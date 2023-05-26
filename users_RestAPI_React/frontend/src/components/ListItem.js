import React from 'react'
import { Link } from 'react-router-dom'


let getTime = (user) => {
    return new Date(user.updated_at).toLocaleDateString()
}

const ListItem = ({user}) => {
    return (
        <Link to={`user/${user.id}`}>
            <div className='users-list-item'>
                <h3>{user.name}</h3>
                <p>
                    <span>
                        {getTime(user)} ~ {user.email}
                    </span>
                </p>
            </div>
        </Link>
    )
}

export default ListItem