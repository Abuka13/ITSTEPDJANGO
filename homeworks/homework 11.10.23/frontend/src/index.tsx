import React from 'react';
import { createRoot } from 'react-dom/client';
// @ts-ignore
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import App from "./App";
import "./css/bootstrap/bootstrap.css";
import "./css/font_awesome/css/all.min.css";
import "./css/my.css";
import HomePage from "./pages/homepage";
import PricingPage from "./pages/pricing";
import RegisterPage from "./pages/register";
import AboutPage from "./pages/about";


const container = document.getElementById('root')!;
const root = createRoot(container);

root.render(
  <Router>
    <Routes>
        <Route path="/" element={<HomePage />}></Route>
        <Route path="/home" element={<HomePage />}></Route>
        <Route path="/pricing" element={<PricingPage />}></Route>
        <Route path="/register" element={<RegisterPage />}></Route>
        <Route path="/about" element={<AboutPage />}></Route>
    </Routes>
  </Router>,
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
