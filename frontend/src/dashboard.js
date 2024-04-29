import React from 'react';

const DashboardPage = () => {
  return (
    <div className={'mainContainer'}>
      <h2>Dashboard</h2>
      <div className="dashboard-content">
        <div className="stats">
          <h3>Statistics</h3>
          <p>Total workouts: 10</p>
          <p>Completed workouts: 8</p>
          <p>Remaining workouts: 2</p>
        </div>
        <div className={'inputContainer'}>
          <h3>Recent Activity</h3>
          <ul>
            <li>Workout on 2024-04-20</li>
            <li>Workout on 2024-04-18</li>
            <li>Workout on 2024-04-16</li>
            <li>...</li>
          </ul>
        </div>
        <div className={'inputContainer'}>
          <h3>Quick Links</h3>
          <ul>
            <li><a href="/workout">Start New Workout</a></li>
            <li><a href="/goals">Set Goals</a></li>
            <li><a href="/profile">View Profile</a></li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;
