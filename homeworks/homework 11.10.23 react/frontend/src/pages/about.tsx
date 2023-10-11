import { Link } from "react-router-dom";
import React from "react";

export default function About() {
    return (
        <body>




<main>
  <h1 className="visually-hidden">Features examples</h1>

  <div className="container px-4 py-5" id="featured-3">
    <h2 className="pb-2 border-bottom">Columns with icons</h2>
    <div className="row g-4 py-5 row-cols-1 row-cols-lg-3">
      <div className="feature col">
        <div className="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
          <svg className="bi" width="1em" height="1em"><use href="#collection"></use></svg>
        </div>
        <h3 className="fs-2 text-body-emphasis">Featured title</h3>
        <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
        <a href="#" className="icon-link">
          Call to action
          <svg className="bi"><use href="#chevron-right"></use></svg>
        </a>
      </div>
      <div className="feature col">
        <div className="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
          <svg className="bi" width="1em" height="1em"><use href="#people-circle"></use></svg>
        </div>
        <h3 className="fs-2 text-body-emphasis">Featured title</h3>
        <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
        <a href="#" className="icon-link">
          Call to action
          <svg className="bi"><use href="#chevron-right"></use></svg>
        </a>
      </div>
      <div className="feature col">
        <div className="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
          <svg className="bi" width="1em" height="1em"><use href="#toggles2"></use></svg>
        </div>
        <h3 className="fs-2 text-body-emphasis">Featured title</h3>
        <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
        <a href="#" className="icon-link">
          Call to action
          <svg className="bi"><use href="#chevron-right"></use></svg>
        </a>
      </div>
    </div>
  </div>

  <div className="b-example-divider"></div>

  <div className="container px-4 py-5" id="hanging-icons">
    <h2 className="pb-2 border-bottom">Hanging icons</h2>
    <div className="row g-4 py-5 row-cols-1 row-cols-lg-3">
      <div className="col d-flex align-items-start">
        <div className="icon-square text-body-emphasis bg-body-secondary d-inline-flex align-items-center justify-content-center fs-4 flex-shrink-0 me-3">
          <svg className="bi" width="1em" height="1em"><use href="#toggles2"></use></svg>
        </div>
        <div>
          <h3 className="fs-2 text-body-emphasis">Featured title</h3>
          <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
          <a href="#" className="btn btn-primary">
            Primary button
          </a>
        </div>
      </div>
      <div className="col d-flex align-items-start">
        <div className="icon-square text-body-emphasis bg-body-secondary d-inline-flex align-items-center justify-content-center fs-4 flex-shrink-0 me-3">
          <svg className="bi" width="1em" height="1em"><use href="#cpu-fill"></use></svg>
        </div>
        <div>
          <h3 className="fs-2 text-body-emphasis">Featured title</h3>
          <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
          <a href="#" className="btn btn-primary">
            Primary button
          </a>
        </div>
      </div>
      <div className="col d-flex align-items-start">
        <div className="icon-square text-body-emphasis bg-body-secondary d-inline-flex align-items-center justify-content-center fs-4 flex-shrink-0 me-3">
          <svg className="bi" width="1em" height="1em"><use href="#tools"></use></svg>
        </div>
        <div>
          <h3 className="fs-2 text-body-emphasis">Featured title</h3>
          <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
          <a href="#" className="btn btn-primary">
            Primary button
          </a>
        </div>
      </div>
    </div>
  </div>

  <div className="b-example-divider"></div>

  <div className="container px-4 py-5" id="custom-cards">
    <h2 className="pb-2 border-bottom">Custom cards</h2>

    <div className="row row-cols-1 row-cols-lg-3 align-items-stretch g-4 py-5">
      <div className="col">
        <div className="card card-cover h-100 overflow-hidden text-bg-dark rounded-4 shadow-lg" >
          <div className="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
            <h3 className="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold">Short title, long jacket</h3>
            <ul className="d-flex list-unstyled mt-auto">
              <li className="me-auto">
                <img src="https://github.com/twbs.png" alt="Bootstrap" width="32" height="32" className="rounded-circle border border-white"/>
              </li>
              <li className="d-flex align-items-center me-3">
                <svg className="bi me-2" width="1em" height="1em"><use href="#geo-fill"></use></svg>
                <small>Earth</small>
              </li>
              <li className="d-flex align-items-center">
                <svg className="bi me-2" width="1em" height="1em"><use href="#calendar3"></use></svg>
                <small>3d</small>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div className="col">
        <div className="card card-cover h-100 overflow-hidden text-bg-dark rounded-4 shadow-lg" >
          <div className="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
            <h3 className="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold">Much longer title that wraps to multiple lines</h3>
            <ul className="d-flex list-unstyled mt-auto">
              <li className="me-auto">
                <img src="https://github.com/twbs.png" alt="Bootstrap" width="32" height="32" className="rounded-circle border border-white"/>
              </li>
              <li className="d-flex align-items-center me-3">
                <svg className="bi me-2" width="1em" height="1em"><use href="#geo-fill"></use></svg>
                <small>Pakistan</small>
              </li>
              <li className="d-flex align-items-center">
                <svg className="bi me-2" width="1em" height="1em"><use href="#calendar3"></use></svg>
                <small>4d</small>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div className="col">
        <div className="card card-cover h-100 overflow-hidden text-bg-dark rounded-4 shadow-lg" >
          <div className="d-flex flex-column h-100 p-5 pb-3 text-shadow-1">
            <h3 className="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold">Another longer title belongs here</h3>
            <ul className="d-flex list-unstyled mt-auto">
              <li className="me-auto">
                <img src="https://github.com/twbs.png" alt="Bootstrap" width="32" height="32" className="rounded-circle border border-white"/>
              </li>
              <li className="d-flex align-items-center me-3">
                <svg className="bi me-2" width="1em" height="1em"><use href="#geo-fill"></use></svg>
                <small>California</small>
              </li>
              <li className="d-flex align-items-center">
                <svg className="bi me-2" width="1em" height="1em"><use href="#calendar3"></use></svg>
                <small>5d</small>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div className="b-example-divider"></div>

  <div className="container px-4 py-5" id="icon-grid">
    <h2 className="pb-2 border-bottom">Icon grid</h2>

    <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 g-4 py-5">
      <div className="col d-flex align-items-start">
        <svg className="bi text-body-secondary flex-shrink-0 me-3" width="1.75em" height="1.75em"><use href="#bootstrap"></use></svg>
        <div>
          <h3 className="fw-bold mb-0 fs-4 text-body-emphasis">Featured title</h3>
          <p>Paragraph of text beneath the heading to explain the heading.</p>
        </div>
      </div>
      <div className="col d-flex align-items-start">
        <svg className="bi text-body-secondary flex-shrink-0 me-3" width="1.75em" height="1.75em"><use href="#cpu-fill"></use></svg>
        <div>
          <h3 className="fw-bold mb-0 fs-4 text-body-emphasis">Featured title</h3>
          <p>Paragraph of text beneath the heading to explain the heading.</p>
        </div>
      </div>
      <div className="col d-flex align-items-start">
        <svg className="bi text-body-secondary flex-shrink-0 me-3" width="1.75em" height="1.75em"><use href="#calendar3"></use></svg>
        <div>
          <h3 className="fw-bold mb-0 fs-4 text-body-emphasis">Featured title</h3>
          <p>Paragraph of text beneath the heading to explain the heading.</p>
        </div>
      </div>
      <div className="col d-flex align-items-start">
        <svg className="bi text-body-secondary flex-shrink-0 me-3" width="1.75em" height="1.75em"><use href="#home"></use></svg>
        <div>
          <h3 className="fw-bold mb-0 fs-4 text-body-emphasis">Featured title</h3>
          <p>Paragraph of text beneath the heading to explain the heading.</p>
        </div>
      </div>
      <div className="col d-flex align-items-start">
        <svg className="bi text-body-secondary flex-shrink-0 me-3" width="1.75em" height="1.75em"><use href="#speedometer2"></use></svg>
        <div>
          <h3 className="fw-bold mb-0 fs-4 text-body-emphasis">Featured title</h3>
          <p>Paragraph of text beneath the heading to explain the heading.</p>
        </div>
      </div>
      <div className="col d-flex align-items-start">
        <svg className="bi text-body-secondary flex-shrink-0 me-3" width="1.75em" height="1.75em"><use href="#toggles2"></use></svg>
        <div>
          <h3 className="fw-bold mb-0 fs-4 text-body-emphasis">Featured title</h3>
          <p>Paragraph of text beneath the heading to explain the heading.</p>
        </div>
      </div>
      <div className="col d-flex align-items-start">
        <svg className="bi text-body-secondary flex-shrink-0 me-3" width="1.75em" height="1.75em"><use href="#geo-fill"></use></svg>
        <div>
          <h3 className="fw-bold mb-0 fs-4 text-body-emphasis">Featured title</h3>
          <p>Paragraph of text beneath the heading to explain the heading.</p>
        </div>
      </div>
      <div className="col d-flex align-items-start">
        <svg className="bi text-body-secondary flex-shrink-0 me-3" width="1.75em" height="1.75em"><use href="#tools"></use></svg>
        <div>
          <h3 className="fw-bold mb-0 fs-4 text-body-emphasis">Featured title</h3>
          <p>Paragraph of text beneath the heading to explain the heading.</p>
        </div>
      </div>
    </div>
  </div>

  <div className="b-example-divider"></div>

  <div className="container px-4 py-5">
    <h2 className="pb-2 border-bottom">Features with title</h2>

    <div className="row row-cols-1 row-cols-md-2 align-items-md-center g-5 py-5">
      <div className="col d-flex flex-column align-items-start gap-2">
        <h2 className="fw-bold text-body-emphasis">Left-aligned title explaining these awesome features</h2>
        <p className="text-body-secondary">Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
        <a href="#" className="btn btn-primary btn-lg">Primary button</a>
      </div>

      <div className="col">
        <div className="row row-cols-1 row-cols-sm-2 g-4">
          <div className="col d-flex flex-column gap-2">
            <div className="feature-icon-small d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-4 rounded-3">
              <svg className="bi" width="1em" height="1em">
                <use href="#collection"></use>
              </svg>
            </div>
            <h4 className="fw-semibold mb-0 text-body-emphasis">Featured title</h4>
            <p className="text-body-secondary">Paragraph of text beneath the heading to explain the heading.</p>
          </div>

          <div className="col d-flex flex-column gap-2">
            <div className="feature-icon-small d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-4 rounded-3">
              <svg className="bi" width="1em" height="1em">
                <use href="#gear-fill"></use>
              </svg>
            </div>
            <h4 className="fw-semibold mb-0 text-body-emphasis">Featured title</h4>
            <p className="text-body-secondary">Paragraph of text beneath the heading to explain the heading.</p>
          </div>

          <div className="col d-flex flex-column gap-2">
            <div className="feature-icon-small d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-4 rounded-3">
              <svg className="bi" width="1em" height="1em">
                <use href="#speedometer"></use>
              </svg>
            </div>
            <h4 className="fw-semibold mb-0 text-body-emphasis">Featured title</h4>
            <p className="text-body-secondary">Paragraph of text beneath the heading to explain the heading.</p>
          </div>

          <div className="col d-flex flex-column gap-2">
            <div className="feature-icon-small d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-4 rounded-3">
              <svg className="bi" width="1em" height="1em">
                <use href="#table"></use>
              </svg>
            </div>
            <h4 className="fw-semibold mb-0 text-body-emphasis">Featured title</h4>
            <p className="text-body-secondary">Paragraph of text beneath the heading to explain the heading.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</main>
<script src="/docs/5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossOrigin="anonymous"></script>



</body>
    );
}