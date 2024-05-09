import React from 'react';
import { useNavigate } from 'react-router-dom';
import {UserContext} from "./App.js"

export const baseUrl = (extension)=>`http://127.0.0.1:5000${extension}`
export const niceFetch = (extension)=>fetch(baseUrl(extension)).then((response)=>response.json())

export const useLoggedIn = ()=>{
  const navigate = useNavigate();
  const [user, setUser] = React.useContext(UserContext);
  React.useEffect(()=>{
    if (user !== undefined) return;
    navigate('/login/');
  }, [user])
  return [user, setUser]
}

const LoginPage = ({ setLoggedIn }) => {
  const navigate = useNavigate();
  const [user, setUser] = React.useContext(UserContext);
  const [userName, setUsername] = React.useState(""); 
  const handleSubmit = (e) => {
    e.preventDefault();
    niceFetch(
      `/api/user_id?name=${userName}`
    ).then(
      ({id})=>niceFetch(`/api/user/${id}`)
    ).then(
      (userWithWorkouts)=>niceFetch(`/api/get_workout_user?user=${userWithWorkouts.userid}`).then((workouts)=>setUser({...userWithWorkouts, workouts})).then(()=>navigate('/dashboard/')))
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
