// SignUpPage.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const SignUpPage = ({ setLoggedIn }) => {
  const navigate = useNavigate();
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Implement sign-up logic here
    // For simplicity, let's just set loggedIn state to true
    setLoggedIn(true);
    // Navigate to the profile page after signing up
    navigate('/profile');
  };

  return (
    <div className={'mainContainer'}>
      <h2>Sign Up</h2>
      <form onSubmit={handleSubmit}>
        <div className={'inputContainer'}>
          <label>First Name:</label>
          <input type="text" value={firstName} onChange={(e) => setFirstName(e.target.value)} className={'inputBox'} />
        </div>
        <div className={'inputContainer'}>
          <label>Last Name:</label>
          <input type="text" value={lastName} onChange={(e) => setLastName(e.target.value)} className={'inputBox'}/>
        </div>
        <div className={'inputContainer'}>
          <label>Email:</label>
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} className={'inputBox'}/>
        </div>
        <div className={'inputContainer'}>
          <label>Password:</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className={'inputBox'}/>
        </div>
        <button className={'inputButton'} type="submit">Sign Up</button>
      </form>
      <button className={'inputButton'} onClick={() => navigate('/profile')}>Go to Profile</button>
    </div>
  );
};

export default SignUpPage;
