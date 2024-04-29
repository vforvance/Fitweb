import React from 'react';

const UserProfilePage = () => {
  // Hardcoded fake user data
  const userProfile = {
    firstName: 'John',
    lastName: 'Doe',
    email: 'john.doe@example.com',
    height: 180,
    weight: 75,
    bio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
  };

  const { firstName, lastName, email, height, weight, bio } = userProfile;

  return (
    <div className="mainContainer">
      <h2>User Profile</h2>
      <div className="userInfo">
        <div>
          <strong>Name:</strong> {firstName} {lastName}
        </div>
        <div>
          <strong>Email:</strong> {email}
        </div>
        <div>
          <strong>Height:</strong> {height} cm
        </div>
        <div>
          <strong>Weight:</strong> {weight} kg
        </div>
        <div>
          <strong>Bio:</strong> {bio}
        </div>
      </div>
    </div>
  );
};

export default UserProfilePage;
