import React, { useState } from 'react';

const GoalSettingPage = () => {
  const [dailyGoal, setDailyGoal] = useState('');
  const [weeklyGoal, setWeeklyGoal] = useState('');
  const [monthlyGoal, setMonthlyGoal] = useState('');

  const handleGoalSubmit = (e) => {
    e.preventDefault();
    // Perform goal submission logic here
    console.log('Submitted goals:', { dailyGoal, weeklyGoal, monthlyGoal });
    // Reset form inputs
    setDailyGoal('');
    setWeeklyGoal('');
    setMonthlyGoal('');
  };

  return (
    <div className={'mainContainer'}>
      <h2>Goal Setting</h2>
      <form onSubmit={handleGoalSubmit}>
        <div className={'inputContainer'}>
          <label htmlFor="daily-goal">Daily Goal:</label>
          <input
            type="text"
            id="daily-goal"
            value={dailyGoal}
            onChange={(e) => setDailyGoal(e.target.value)}
            placeholder="Enter daily goal"
          />
        </div>
        <div className={'inputContainer'}>
          <label htmlFor="weekly-goal">Weekly Goal:</label>
          <input
            type="text"
            id="weekly-goal"
            value={weeklyGoal}
            onChange={(e) => setWeeklyGoal(e.target.value)}
            placeholder="Enter weekly goal"
          />
        </div>
        <div className={'inputContainer'}>
          <label htmlFor="monthly-goal">Monthly Goal:</label>
          <input
            type="text"
            id="monthly-goal"
            value={monthlyGoal}
            onChange={(e) => setMonthlyGoal(e.target.value)}
            placeholder="Enter monthly goal"
          />
        </div>
        <button className={'inputButton'} type="submit">Set Goals</button>
      </form>
    </div>
  );
};

export default GoalSettingPage;
