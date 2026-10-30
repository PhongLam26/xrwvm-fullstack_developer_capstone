const express = require("express");
const mongoose = require("mongoose");
const fs = require("fs");
const path = require("path");

const app = express();
const port = Number(process.env.PORT || 3030);
const mongoUrl = process.env.MONGO_URL || "mongodb://127.0.0.1:27017/dealershipsDB";

app.use(express.json({ limit: "32kb" }));

const Reviews = require("./review");
const Dealerships = require("./dealership");

function readSeedFile(fileName, property) {
  const filePath = path.join(__dirname, "data", fileName);
  return JSON.parse(fs.readFileSync(filePath, "utf8"))[property] || [];
}

async function seedCollections() {
  const dealerships = readSeedFile("dealerships.json", "dealerships");
  const reviews = [
    ...readSeedFile("reviews.json", "reviews"),
    ...readSeedFile("demo_reviews.json", "reviews"),
  ];

  if ((await Dealerships.countDocuments()) === 0 && dealerships.length) {
    await Dealerships.insertMany(dealerships);
    console.log("Seeded " + dealerships.length + " IBM dealership records.");
  }
  if ((await Reviews.countDocuments()) === 0 && reviews.length) {
    await Reviews.insertMany(reviews);
    console.log(
      "Seeded " + reviews.length + " reviews, including the documented Kansas demo review."
    );
  }
}

app.get("/", (_req, res) => {
  res.json({ service: "Cars Dealership API", status: "ok" });
});

app.get("/health", (_req, res) => {
  res.json({ status: mongoose.connection.readyState === 1 ? "ok" : "starting" });
});

app.get("/fetchReviews", async (_req, res, next) => {
  try {
    res.json(await Reviews.find().sort({ id: 1 }).lean());
  } catch (error) {
    next(error);
  }
});

app.get("/fetchReviews/dealer/:id", async (req, res, next) => {
  const dealerId = Number(req.params.id);
  if (!Number.isInteger(dealerId) || dealerId < 1) {
    return res.status(400).json({ error: "Dealer ID must be a positive integer." });
  }
  try {
    res.json(
      await Reviews.find({ dealership: dealerId }).sort({ id: 1 }).lean()
    );
  } catch (error) {
    next(error);
  }
});

app.get("/fetchDealers", async (_req, res, next) => {
  try {
    res.json(await Dealerships.find().sort({ id: 1 }).lean());
  } catch (error) {
    next(error);
  }
});

app.get("/fetchDealers/:state", async (req, res, next) => {
  const state = req.params.state.trim();
  if (!/^[a-z ]+$/i.test(state)) {
    return res.status(400).json({ error: "State contains unsupported characters." });
  }
  try {
    res.json(
      await Dealerships.find({
        state: { $regex: "^" + state + "$", $options: "i" },
      })
        .sort({ id: 1 })
        .lean()
    );
  } catch (error) {
    next(error);
  }
});

app.get("/fetchDealer/:id", async (req, res, next) => {
  const dealerId = Number(req.params.id);
  if (!Number.isInteger(dealerId) || dealerId < 1) {
    return res.status(400).json({ error: "Dealer ID must be a positive integer." });
  }
  try {
    const dealer = await Dealerships.findOne({ id: dealerId }).lean();
    if (!dealer) {
      return res.status(404).json({ error: "Dealer " + dealerId + " was not found." });
    }
    return res.json([dealer]);
  } catch (error) {
    return next(error);
  }
});

app.post("/insert_review", async (req, res, next) => {
  const required = [
    "name",
    "dealership",
    "review",
    "purchase_date",
    "car_make",
    "car_model",
    "car_year",
  ];
  if (required.some((field) => req.body[field] === undefined || req.body[field] === "")) {
    return res.status(400).json({ error: "All review fields are required." });
  }

  try {
    const dealerId = Number(req.body.dealership);
    const carYear = Number(req.body.car_year);
    if (!Number.isInteger(dealerId) || !Number.isInteger(carYear)) {
      return res.status(400).json({ error: "Dealer ID and car year must be integers." });
    }
    if (!(await Dealerships.exists({ id: dealerId }))) {
      return res.status(404).json({ error: "Dealer " + dealerId + " was not found." });
    }
    const latest = await Reviews.findOne().sort({ id: -1 }).select({ id: 1 }).lean();
    const review = await Reviews.create({
      id: (latest?.id || 0) + 1,
      name: String(req.body.name).trim(),
      dealership: dealerId,
      review: String(req.body.review).trim(),
      purchase: Boolean(req.body.purchase),
      purchase_date: String(req.body.purchase_date),
      car_make: String(req.body.car_make).trim(),
      car_model: String(req.body.car_model).trim(),
      car_year: carYear,
      sentiment: req.body.sentiment,
    });
    return res.status(201).json(review.toObject());
  } catch (error) {
    return next(error);
  }
});

// Express identifies error middleware by its four parameters.
/* jshint unused: false */
app.use((error, _req, res, _next) => {
  console.error(error);
  res.status(500).json({ error: "The dealership service could not complete the request." });
});

async function start() {
  await mongoose.connect(mongoUrl);
  await seedCollections();
  return app.listen(port, () => {
    console.log("Cars Dealership API listening on http://localhost:" + port);
  });
}

if (require.main === module) {
  start().catch((error) => {
    console.error("Could not start the dealership API:", error.message);
    process.exitCode = 1;
  });
}

module.exports = { app, start };
