import React, { useState } from 'react';
import { UserContext } from './App';
import { useNiceFetch } from './dashboard';
import { niceFetch, useLoggedIn } from './login';

const WorkoutTrackingPage = () => {

  const [user, setUser] = useLoggedIn() ;
  const [activeWorkout, setActiveWorkout] = React.useState(undefined);
  const handleTrackingSubmit = (e) => {
    e.preventDefault();
  };
  //console.log(user.workouts, 'ww')
  const [workouts, setWorkouts] = React.useState(user?.workouts);
  React.useEffect(()=>setWorkouts(user?.workouts), [user?.workouts]);

  return user !== undefined && (  
    <div style={{width: "100%"}}>
      <div className="split left">
      <ExerciseByName userid={user.userid} setWorkout={
        (newWorkouts)=>{
          setWorkouts(newWorkouts); 
          setActiveWorkout(undefined);
        }} defaultWorkouts={user?.workouts}/>  
      <h2 className='container'>Workouts</h2>
      {user !== undefined && (
      <ul className='color:black'>{(workouts).map((data, index)=>{
        return (<li onClick={()=>setActiveWorkout(index)} className={`listcontainer ${index === activeWorkout ? "highlight" : ""}`}>{data.name}</li>)
        })}</ul>)}
      </div>
      <div className="split right">
      <h2 className='container'>Logs</h2>
      {user !== undefined && activeWorkout !== undefined && workouts[activeWorkout] && (
      <ul className='color:black'>{(workouts[activeWorkout].logs).map((data)=><RenderExercise log={data}/>)}</ul>)}
      </div>
    </div>
  );
};

const RenderExercise = ({log})=>{
  const [exercise, setExercise] = React.useState(undefined);
  useNiceFetch(`/api/exercise/${log.exerciseid}`, setExercise);
  return (exercise === undefined ? undefined : (<li className='listcontainerwork'>{exercise.name}<br/>Reps: {log.rep}<br/>Sets: {log.set}<br/>Weight: {log.weight}</li>))
}

const ExerciseByName = ({userid, setWorkout, defaultWorkouts})=>{
  const [value, setValue] = React.useState(undefined);
  return <>
  <input type='text' onChange={(event)=>{
    console.log(event);
    setValue(event.target.value);
    }}/>
  <button onClick={()=>niceFetch(`/api/get_workout_name?user=${userid}&name=${value}`).then(setWorkout)}>Search</button>
  <button onClick={()=>setWorkout(defaultWorkouts)}>Reset</button>
  </>
}
export default WorkoutTrackingPage;
