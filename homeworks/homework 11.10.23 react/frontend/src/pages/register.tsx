import { Link } from "react-router-dom";
import React from "react";

export default function Register() {
    return (

<body className="d-flex align-items-center py-4 bg-body-tertiary">





<main className="form-signin w-100 m-auto">
  <form>
    <img
          className="d-block mx-auto mb-4"
          src="https://getbootstrap.com/docs/5.3/assets/brand/bootstrap-logo.svg"
          alt=""
          width="72"
          height="57"
        />
    <h1 className="h3 mb-3 fw-normal">Please sign in</h1>

    <div className="form-floating">
      <input type="email" className="form-control" id="floatingInput" placeholder="name@example.com"/>
      <label htmlFor="floatingInput">Email address</label>
    </div>
    <div className="form-floating">
      <input type="password" className="form-control" id="floatingPassword" placeholder="Password"/>
      <label htmlFor="floatingPassword">Password</label>
    </div>
    <div className="form-floating">
      <input type="password" className="form-control" id="floatingPassword" placeholder="Password"/>
      <label htmlFor="floatingPassword">Repeat Password</label>
    </div>

    <div className="form-check text-start my-3">
      <input className="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault"/>
      <label className="form-check-label" htmlFor="flexCheckDefault">
        Remember me
      </label>
    </div>
    <button className="btn btn-primary w-100 py-2" type="submit">Sign in</button>
            <button type="button" className="btn btn-warning">
              <Link to={"/home"} className="nav-link px-2 text-white">
                Дом
              </Link>
            </button>

    <p className="mt-5 mb-3 text-body-secondary">© 2017–2023</p>
  </form>
</main>

<script src="/docs/5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossOrigin="anonymous"></script>



</body>

    );
}