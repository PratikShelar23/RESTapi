import React from 'react'

const Company = (props) => {
  return (
    <div className='company'>
        <h1>{props.name}</h1>
        <h4>{props.location}</h4>
        <p>{props.type}</p>
        <p>{props.about}</p>

    </div>
  )
}

export default Company