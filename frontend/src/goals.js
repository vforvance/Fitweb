import React, { useState } from 'react';
import { useNiceFetch } from './dashboard';

const GoalSettingPage = () => {
  const [response, setResponse] = React.useState(undefined);
  useNiceFetch('/api/max_weights/', setResponse);
  return (
    <div className={'mainContainer'}>
      <h2>Goal Setting</h2>
      <form>
        {/* Form for setting daily, weekly, and monthly goals */}
      </form>

      {/* Leaderboard section */}
      <div className="leaderboard">
        <h3>Leaderboard</h3>
        <table border={"black"}>
          <thead>
            <tr>
              <th style={{padding: "0.25rem"}}>Exercise</th>
              <th style={{padding: "0.25rem"}}>Username</th>
              <th style={{padding: "0.25rem"}}>Highest Lifted Weight (kg)</th>
            </tr>
          </thead>
          <tbody>
            {response === undefined ? undefined : response.items.map(([excericse, name, weight ], index)=>(<tr key={index}>
               <td style={{padding: "0.25rem"}}>{excericse}</td> 
               <td style={{padding: "0.25rem"}}>{name}</td>
               <td style={{padding: "0.25rem"}}>{weight}</td>
            </tr>))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default GoalSettingPage;
