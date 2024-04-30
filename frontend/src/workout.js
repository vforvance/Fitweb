import React, { useState } from 'react';
import { UserContext } from './App';
import { useNiceFetch } from './dashboard';

const WorkoutTrackingPage = () => {

  const [user, setUser] = React.useContext(UserContext);
  const [activeWorkout, setActiveWorkout] = React.useState(undefined);
  const handleTrackingSubmit = (e) => {
    e.preventDefault();
  };
  //console.log(user.workouts, 'ww')
  return (
    <div style={{width: "100%"}}>
      <div className="split left">
      <h2 className='container'>Workouts</h2>
      {user !== undefined && (
      <ul className='color:black'>{(user.workouts).map((data, index)=>{
        return (<li onClick={()=>setActiveWorkout(index)} className={`listcontainer ${index === activeWorkout ? "highlight" : ""}`}>{data.name}</li>)
        })}</ul>)}
      </div>
      <div className="split right">
      <h2 className='container'>Logs</h2>
      {user !== undefined && activeWorkout !== undefined && (
      <ul className='color:black'>{(user.workouts[activeWorkout].logs).map((data)=><RenderExercise log={data}/>)}</ul>)}
      </div>
    </div>
  );
};

const RenderExercise = ({log})=>{
  const [exercise, setExercise] = React.useState(undefined);
  useNiceFetch(log.exerciseid, setExercise);
  return (exercise === undefined ? undefined : (<li className='listcontainerwork'>{exercise.name}<br/>Reps: {log.rep}<br/>Sets: {log.set}<br/>Weight: {log.weight}</li>))
}
export default WorkoutTrackingPage;
