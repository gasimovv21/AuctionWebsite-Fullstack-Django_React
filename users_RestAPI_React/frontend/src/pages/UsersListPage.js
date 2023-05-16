import React, { useEffect, useState } from 'react'
import AddButton from '../components/AddButton'
import ListItem from '../components/ListItem'

const UsersListPage = () => {

    let [users, setUsers] = useState([])

    useEffect(() => {
        getUsers()
    }, [])


    let getUsers = async () => {
        let response = await fetch('/api/users/')
        let data = await response.json()
        console.log('DATA:', data)
        setUsers(data)
    }

    return (
        <div className='users'>
            <div className='users-header'>
                <h2 className='users-title'>&#9782; Users</h2>
                <p className='users-count'>{users.length}</p>
            </div>

            <div className='users-list'>
                {users.map((user, index) => (
                        <ListItem key={index} user={user} />
                ))}
            </div>
            <AddButton />
        </div>
    )
}

export default UsersListPage