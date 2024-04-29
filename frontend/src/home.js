import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Home = () => {
  const [loggedIn, setLoggedIn] = useState(false);
  const navigate = useNavigate(); // Initialize navigate from useNavigate hook

  const handleLogin = () => {
    // Simulated login logic
    setLoggedIn(true);
    console.log('User logged in:', loggedIn); // Log the updated state
    navigate('/login'); // Navigate to profile page
  };

  const handleLogout = () => {
    // Simulated logout logic
    setLoggedIn(false);
    console.log('User logged out:', loggedIn); // Log the updated state
  };

  return (
    <div className={'mainContainer'}>
      {loggedIn ? (
        <div className={'titleContainer'}>
          <p>Welcome, User!</p>
          <button className={'inputButton'} onClick={handleLogout}>Logout</button>
        </div>
      ) : (
        <div>
          <p>Please log in</p>
          <button onClick={handleLogin}>Login</button>
        </div>
      )}
    </div>
  );
};

export default Home;
