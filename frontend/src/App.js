import React, { useState, createContext } from 'react';
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

export const UserContext = createContext();

function App() {
  const [user, setUser] = useState(undefined);
  return (
    <div className="App">
      <UserContext.Provider value={[user, setUser]}>
      <BrowserRouter>
        <Navbar loggedIn={false}/>
        <Routes>
          <Route path="/login" element={<LoginPage setLoggedIn={false} />} />
          <Route path="/dashboard" element={<DashboardPage />} />
          <Route path="/profile" element={<UserProfilePage />} />
          <Route path="/goals" element={<GoalSettingPage />} />
          <Route path="/workout" element={<WorkoutTrackingPage />} />
        </Routes>
      </BrowserRouter>
      </UserContext.Provider>
    </div>
  );
}

export default App;
