// LoginPage.jsx
import React from 'react';
import { useNavigate } from 'react-router-dom';

const LoginPage = ({ setLoggedIn }) => {
  const navigate = useNavigate();

  const handleSignup = () => {
    // Navigate to the sign-up page
    navigate('/signup');
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Implement login logic here
    // For simplicity, let's just set loggedIn state to true
    setLoggedIn(true);
    // Navigate to the dashboard
    navigate('/dashboard');
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        {/* Your login form inputs */}
        <button type="submit">Login</button>
      </form>
      <div>
        <p>Don't have an account? <button onClick={handleSignup}>Sign Up</button></p>
      </div>
    </div>
  );
};

export default LoginPage;
