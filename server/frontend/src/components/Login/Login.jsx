import React, { useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import Header from "../Header/Header";
import { apiFetch, responseJson } from "../../api";

const Login = () => {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();

  const login = async (event) => {
    event.preventDefault();
    setError("");
    setBusy(true);
    try {
      const result = await responseJson(
        await apiFetch("/djangoapp/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ userName, password }),
        })
      );
      sessionStorage.setItem("username", result.userName);
      sessionStorage.setItem("firstName", result.firstName || "");
      sessionStorage.setItem("lastName", result.lastName || "");
      const next = new URLSearchParams(location.search).get("next") || "/";
      navigate(next.startsWith("/") ? next : "/", { replace: true });
    } catch (requestError) {
      setError(requestError.message);
    } finally {
      setBusy(false);
    }
  };

  return (
    <>
      <Header />
      <main className="page-shell narrow">
        <section className="form-card">
          <p className="eyebrow">Welcome back</p>
          <h1>Log in to your account</h1>
          <p className="muted">Sign in to write a review and manage your session.</p>
          {error && <p className="form-message error" role="alert">{error}</p>}
          <form onSubmit={login}>
            <label htmlFor="username">Username</label>
            <input
              id="username"
              name="username"
              autoComplete="username"
              required
              value={userName}
              onChange={(event) => setUserName(event.target.value)}
            />
            <label htmlFor="password">Password</label>
            <input
              id="password"
              name="password"
              type="password"
              autoComplete="current-password"
              required
              value={password}
              onChange={(event) => setPassword(event.target.value)}
            />
            <button className="button button-primary button-wide" disabled={busy} type="submit">
              {busy ? "Signing in…" : "Log in"}
            </button>
          </form>
          <p className="form-footnote">New here? <Link to="/register">Create an account</Link></p>
        </section>
      </main>
    </>
  );
};

export default Login;
