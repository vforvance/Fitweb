import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const LoginPage = ({ setLoggedIn }) => {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Implement login logic here
    // For simplicity, let's just set loggedIn state to true
    setLoggedIn(true);
    // Navigate to the dashboard of the specified user
    navigate(`/dashboard/${username}`);
  };

  return (
    <div className={'mainContainer'}>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div className={'inputContainer'}>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Enter username"
          />
        </div>
        <button className={'inputButton'} type="submit">Login</button>
      </form>
    </div>
  );
};

export default LoginPage;
