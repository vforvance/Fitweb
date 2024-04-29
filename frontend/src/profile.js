import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const UserProfilePage = () => {
  // Define state for user profile information
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [bio, setBio] = useState('');

  // Function to handle profile update
  const handleProfileUpdate = (e) => {
    e.preventDefault();
    // Perform profile update logic here
    console.log('Updated profile:', { username, email, bio });
    // You can add logic to update the user profile on the server here
  };

  return (
    <div className={'mainContainer'}>
      <h2>User Profile</h2>
      <form onSubmit={handleProfileUpdate}>
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
        <div className={'inputContainer'}>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter email"
          />
        </div>
        <div className={'inputContainer'}>
          <label htmlFor="bio">Bio:</label>
          <textarea
            id="bio"
            value={bio}
            onChange={(e) => setBio(e.target.value)}
            placeholder="Enter bio"
          ></textarea>
        </div>
        <button className={'inputButton'} type="submit">Update Profile</button>
      </form>
    </div>
  );
};

export default UserProfilePage;
