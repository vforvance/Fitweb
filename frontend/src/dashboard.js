import React from 'react';
import { useOutletContext } from "react-router-dom";
import { UserContext } from './App';
import { niceFetch } from './login';
import { Link } from 'react-router-dom';

export const useNiceFetch = (extension, setter)=>{
  React.useEffect(()=>{
    if (extension === undefined) return;
    niceFetch(extension).then((data)=>{
      if (destructorCalled) return;
      setter(data);
    })
    let destructorCalled = false;
    return ()=>{
      destructorCalled = true;
    }
  }, [extension, setter]);
}

const DashboardPage = () => {

  const [user, setUser] = React.useContext(UserContext);
  const [personalBest, setPersonalBest] = React.useState(undefined);
  useNiceFetch(user === undefined ? undefined : `/api/personal_best/${user.userid}`, setPersonalBest);
  console.log(user);
  return (
    <div className={'mainContainer'}>
      {user !== undefined && <>
      <h2>{`${user.username} Dashboard`}</h2>
      <div className="dashboard-content">
        {personalBest !== undefined &&
        <div className="stats">
          <h3>Personal Bests</h3>
          <ul>{Object.entries(personalBest).map(([name, weight])=><li>{name}: {weight}</li>)}
          </ul>
        </div>}
        <div className={'inputContainer'}>
          <h3>Quick Links</h3>
          <ul>
            <li><Link to="/workout">Workout</Link></li>
            <li><Link to="/goals">Goals</Link></li>
            <li><Link to="/profile">Profile</Link></li>
          </ul>
        </div>
      </div>
      </>
}
    </div>
  );
};

export default DashboardPage;
