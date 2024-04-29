import React, { useState } from 'react';

const GoalSettingPage = () => {
  const [dailyGoal, setDailyGoal] = useState('');
  const [weeklyGoal, setWeeklyGoal] = useState('');
  const [monthlyGoal, setMonthlyGoal] = useState('');

  // Hardcoded fake user information for leaderboard
  const leaderboardData = [
    { username: 'John', deadlift: 200, squat: 180, shoulderPress: 100, pullUp: 15, barbellRow: 150, bicepCurl: 50 },
    { username: 'Alice', deadlift: 220, squat: 170, shoulderPress: 110, pullUp: 8, barbellRow: 120, bicepCurl: 45 },
    { username: 'Bob', deadlift: 210, squat: 185, shoulderPress: 105, pullUp: 16, barbellRow: 145, bicepCurl: 52 },
    // Add more fake user information as needed
  ];

  // Function to find the user with the highest lifted weight for each exercise
  const findLeader = (exercise) => {
    let maxWeight = -1;
    let leader = null;
    leaderboardData.forEach((user) => {
      if (user[exercise] > maxWeight) {
        maxWeight = user[exercise];
        leader = user;
      }
    });
    return leader;
  };

  return (
    <div className={'mainContainer'}>
      <h2>Goal Setting</h2>
      <form>
        {/* Form for setting daily, weekly, and monthly goals */}
      </form>

      {/* Leaderboard section */}
      <div className="leaderboard">
        <h3>Leaderboard</h3>
        <table>
          <thead>
            <tr>
              <th>Exercise</th>
              <th>Username</th>
              <th>Highest Lifted Weight (kg)</th>
            </tr>
          </thead>
          <tbody>
            {Object.keys(leaderboardData[0]).slice(1).map((exercise, index) => (
              <tr key={index}>
                <td>{exercise}</td>
                <td>{findLeader(exercise).username}</td>
                <td>{findLeader(exercise)[exercise]}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default GoalSettingPage;
