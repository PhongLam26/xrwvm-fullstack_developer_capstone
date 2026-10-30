import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Header from "../Header/Header";
import { apiFetch, responseJson } from "../../api";

const Register = () => {
  const [form, setForm] = useState({
    username: "",
    first_name: "",
    last_name: "",
    email: "",
    password: "",
  });
  const [message, setMessage] = useState("");
  const [isError, setIsError] = useState(false);
  const [busy, setBusy] = useState(false);
  const navigate = useNavigate();

  const update = (event) => {
    setForm({ ...form, [event.target.name]: event.target.value });
  };

  const submit = async (event) => {
    event.preventDefault();
    setMessage("");
    setIsError(false);
    setBusy(true);
    try {
      await responseJson(
        await apiFetch("/djangoapp/register", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(form),
        })
      );
      setMessage("Your account has been created. You can now log in.");
      window.setTimeout(() => navigate("/login"), 900);
    } catch (requestError) {
      setIsError(true);
      setMessage(requestError.message);
    } finally {
      setBusy(false);
    }
  };

  return (
    <>
      <Header />
      <main className="page-shell narrow">
        <section className="form-card">
          <p className="eyebrow">Join the community</p>
          <h1>Create an account</h1>
          <p className="muted">Share your dealership experience with other drivers.</p>
          {message && (
            <p className={"form-message " + (isError ? "error" : "success")} role="status">
              {message}
            </p>
          )}
          <form onSubmit={submit}>
            <label htmlFor="register-username">Username</label>
            <input id="register-username" name="username" autoComplete="username" required maxLength="150" value={form.username} onChange={update} />
            <div className="form-grid">
              <div>
                <label htmlFor="first-name">First Name</label>
                <input id="first-name" name="first_name" autoComplete="given-name" required value={form.first_name} onChange={update} />
              </div>
              <div>
                <label htmlFor="last-name">Last Name</label>
                <input id="last-name" name="last_name" autoComplete="family-name" required value={form.last_name} onChange={update} />
              </div>
            </div>
            <label htmlFor="email">Email</label>
            <input id="email" name="email" type="email" autoComplete="email" required value={form.email} onChange={update} />
            <label htmlFor="register-password">Password</label>
            <input id="register-password" name="password" type="password" autoComplete="new-password" minLength="8" required value={form.password} onChange={update} />
            <button className="button button-primary button-wide" disabled={busy} type="submit">
              {busy ? "Creating account…" : "Register"}
            </button>
          </form>
          <p className="form-footnote">Already registered? <Link to="/login">Log in</Link></p>
        </section>
      </main>
    </>
  );
};

export default Register;
