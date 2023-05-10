import React, { useEffect, useState } from 'react'
import ListItem from '../components/ListItem'

const UsersListPage = () => {

    let [users, setUsers] = useState([])

    useEffect(() => {
        getUsers()
    }, [])


    let getUsers = async () => {
        let response = await fetch('http://127.0.0.1:8000/api/users/')
        let data = await response.json()
        console.log('DATA:', data)
        setUsers(data)
    }

    return (
        <div>
            <div className='users-list'>
                {users.map((user, index) => (
                        <ListItem key={index} user={user} />
                ))}
            </div>
        </div>
    )
}

export default UsersListPage