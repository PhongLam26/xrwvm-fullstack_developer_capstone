import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { apiFetch, responseJson } from "../../api";

const Header = () => {
  const [username, setUsername] = useState(sessionStorage.getItem("username") || "");
  const navigate = useNavigate();

  const logout = async () => {
    try {
      await responseJson(
        await apiFetch("/djangoapp/logout", { method: "POST" })
      );
      sessionStorage.removeItem("username");
      sessionStorage.removeItem("firstName");
      sessionStorage.removeItem("lastName");
      setUsername("");
      navigate("/", { replace: true });
    } catch (error) {
      window.alert(error.message);
    }
  };

  return (
    <header className="site-header">
      <div className="nav-wrap">
        <Link className="brand" to="/" aria-label="Cars Dealership home">
          <span className="brand-mark">CD</span>
          <span>Cars Dealerships</span>
        </Link>
        <nav aria-label="Main navigation">
          <Link to="/">Dealers</Link>
          <a href="/about">About Us</a>
          <a href="/contact">Contact Us</a>
        </nav>
        <div className="account-nav">
          {username ? (
            <>
              <span className="signed-in">Signed in as <strong>{username}</strong></span>
              <button className="button button-quiet" onClick={logout} type="button">
                Log out
              </button>
            </>
          ) : (
            <>
              <Link to="/login">Log in</Link>
              <Link className="button button-small" to="/register">Create account</Link>
            </>
          )}
        </div>
      </div>
    </header>
  );
};

export default Header;
