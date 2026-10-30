function readCookie(name) {
  const prefix = name + "=";
  const entry = document.cookie
    .split(";")
    .map((item) => item.trim())
    .find((item) => item.startsWith(prefix));
  return entry ? decodeURIComponent(entry.slice(prefix.length)) : "";
}

export async function apiFetch(url, options = {}) {
  const method = (options.method || "GET").toUpperCase();
  const headers = new Headers(options.headers || {});
  if (!["GET", "HEAD", "OPTIONS", "TRACE"].includes(method)) {
    let token = readCookie("csrftoken");
    if (!token) {
      const response = await fetch("/djangoapp/csrf", {
        credentials: "same-origin",
      });
      if (!response.ok) {
        throw new Error("Could not prepare a secure form submission.");
      }
      token = readCookie("csrftoken");
    }
    if (token) {
      headers.set("X-CSRFToken", token);
    }
  }
  return fetch(url, {
    ...options,
    method,
    headers,
    credentials: "same-origin",
  });
}

export async function responseJson(response) {
  const payload = await response.json();
  if (!response.ok) {
    throw new Error(payload.error || "The request could not be completed.");
  }
  return payload;
}
