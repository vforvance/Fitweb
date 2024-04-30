import React from 'react';
import { useNavigate, Outlet } from 'react-router-dom';
import {UserContext} from "./App.js"

export const baseUrl = (extension)=>`http://127.0.0.1:5000${extension}`
export const niceFetch = (extension)=>fetch(baseUrl(extension)).then((response)=>response.json())

const LoginPage = ({ setLoggedIn }) => {
  const navigate = useNavigate();
  const [user, setUser] = React.useContext(UserContext);
  const [userName, setUsername] = React.useState(""); 
  const handleSubmit = (e) => {
    e.preventDefault();
    niceFetch(`/api/user_id?name=${userName}`).then(({id})=>niceFetch(`/api/user/${id}`)).then(setUser)
    // Implement login logic here
    // For simplicity, let's just set loggedIn state to true
    //setLoggedIn(true);
    // Navigate to the dashboard of the specified user
    navigate(`/dashboard/`);
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
            value={userName}
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
