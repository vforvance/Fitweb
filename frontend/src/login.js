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
    <div className={'mainContainer'}>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        {/* Your login form inputs */}
        <button className={'inputButton'} type="submit" >Login</button>
      </form>
      <div className={'inputContainer'}>
        <p>Don't have an account? <button className={'inputButton'} type="submit" onClick={handleSignup}>Sign Up</button></p>
      </div>
    </div>
  );
};

export default LoginPage;
