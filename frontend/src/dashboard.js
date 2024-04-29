import React from 'react';

const DashboardPage = () => {
  // Hardcoded personal best data for Jon
  const personalBests = {
    deadlift: 250,
    squat: 220,
    shoulderPress: 120,
    barbellRow: 180,
    bicepCurl: 60,
    pullUp: 20,
  };

  return (
    <div className={'mainContainer'}>
      <h2>Jon's Dashboard</h2>
      <div className="dashboard-content">
        <div className="stats">
          <h3>Personal Bests</h3>
          <ul>
            <li>Deadlift: {personalBests.deadlift} kg</li>
            <li>Squat: {personalBests.squat} kg</li>
            <li>Shoulder Press: {personalBests.shoulderPress} kg</li>
            <li>Barbell Row: {personalBests.barbellRow} kg</li>
            <li>Bicep Curl: {personalBests.bicepCurl} kg</li>
            <li>Pull-Up: {personalBests.pullUp} reps</li>
          </ul>
        </div>
        <div className={'inputContainer'}>
          <h3>Quick Links</h3>
          <ul>
            <li><a href="/workout">New Workout</a></li>
            <li><a href="/goals">Set Goals</a></li>
            <li><a href="/profile">View Profile</a></li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;
