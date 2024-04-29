import React, { useState } from 'react';

const WorkoutTrackingPage = () => {
  const [exercise, setExercise] = useState('');
  const [duration, setDuration] = useState('');
  const [caloriesBurned, setCaloriesBurned] = useState('');

  const handleTrackingSubmit = (e) => {
    e.preventDefault();
    // Perform workout tracking submission logic here
    console.log('Tracked workout:', { exercise, duration, caloriesBurned });
    // Reset form inputs
    setExercise('');
    setDuration('');
    setCaloriesBurned('');
  };

  return (
    <div className={'mainContainer'}>
      <h2>Workout Tracking</h2>
      <form onSubmit={handleTrackingSubmit}>
        <div className={'inputContainer'}>
          <label htmlFor="exercise">Exercise:</label>
          <input
            type="text"
            id="exercise"
            value={exercise}
            onChange={(e) => setExercise(e.target.value)}
            placeholder="Enter exercise"
          />
        </div>
        <div className={'inputContainer'}>
          <label htmlFor="duration">Duration (minutes):</label>
          <input
            type="number"
            id="duration"
            value={duration}
            onChange={(e) => setDuration(e.target.value)}
            placeholder="Enter duration"
          />
        </div>
        <div className={'inputContainer'}>
          <label htmlFor="calories-burned">Calories Burned:</label>
          <input
            type="number"
            id="calories-burned"
            value={caloriesBurned}
            onChange={(e) => setCaloriesBurned(e.target.value)}
            placeholder="Enter calories burned"
          />
        </div>
        <button className={'inputButton'} type="submit">Track Workout</button>
      </form>
    </div>
  );
};

export default WorkoutTrackingPage;
