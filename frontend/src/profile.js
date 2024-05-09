import React from 'react';
import { UserContext } from './App';
import { useLoggedIn } from './login';

const UserProfilePage = () => {
  
  const [user, setUser] = useLoggedIn();
 

  //const { firstName, lastName, email, height, weight, bio } = userProfile;

  return user !== undefined && (
    <div className="mainContainer">
      <h2>User Profile</h2>
      <div className="userInfo">
        <div>
          <strong>Name:</strong> {user.firstname} {user.lastname}
        </div>
        <div>
          <strong>Email:</strong> {user.email}
        </div>
        <div>
          <strong>Height:</strong> {user.height} cm
        </div>
        <div>
          <strong>Weight:</strong> {user.weight} kg
        </div>
        <div>
          <strong>Bio:</strong> {user.fitnessgoal}
        </div>
      </div>
    </div>
  );
};

export default UserProfilePage;
