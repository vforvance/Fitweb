import React, { useState } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Home from './home';
import LoginPage from './login';
import DashboardPage from './dashboard'; 
import UserProfilePage from './profile';
import GoalSettingPage from './goals';
import WorkoutTrackingPage from './workout';
import Navbar from './Navbar';
import SignUpPage from './signup';
import './App.css';

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [email, setEmail] = useState('');

  return (
    <div className="App">
      <BrowserRouter>
        <Navbar loggedIn={loggedIn} />
        <Routes>
          <Route path="/" element={<Home email={email} loggedIn={loggedIn} setLoggedIn={setLoggedIn} />} />
          <Route path="/login" element={<LoginPage setLoggedIn={setLoggedIn} />} />
          <Route path="/dashboard" element={<DashboardPage />} />
          <Route path="/profile" element={<UserProfilePage />} />
          <Route path="/goals" element={<GoalSettingPage />} />
          <Route path="/workout" element={<WorkoutTrackingPage />} />
          <Route path="/signup" element={<SignUpPage setLoggedIn={setLoggedIn} />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
