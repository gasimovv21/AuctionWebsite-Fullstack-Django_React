import Cookies from 'js-cookie';
import React, { useEffect, useState } from 'react';
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg';


const UserPage = ({ match, history }) => {

    let userId = match.params.id
    let [user, setUser] = useState(null)

    useEffect(() => {
        getUser()
    }, [userId])

    let getUser = async () => {
        if (userId === 'new') return


        let reponse = await fetch(`/api/users/${userId}`)
        let data = await reponse.json()
        setUser(data)
    }


    let updateUser = async () => {
        const csrftoken = Cookies.get('csrftoken');
    
        fetch(`/api/users/${userId}/update/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify(user),
        });
    };

    let createUser = async () => {
        const csrftoken = Cookies.get('csrftoken');

        fetch(`/api/users/create/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body:JSON.stringify(user)
            
        })
        history.push('/')
    }


    let deleteUser = async () => {
        const csrftoken = Cookies.get('csrftoken');

        fetch(`/api/users/${userId}/delete/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            }
        })
        history.push('/')
    }


    let handleSubmit = () => {
        updateUser()
        history.push('/')
    }


    return (
        <div className='user'>
            <div className='user-header'>
                <h3>
                    <ArrowLeft onClick={handleSubmit} />
                </h3>
                {userId !== 'new' ? (
                    <button onClick={deleteUser}>Delete</button>
                ) : (
                    <button onClick={createUser}>Done</button>
                )}
            </div>
            <h2 className='user-info-header'>
                Name <textarea 
                    onChange={(e) => { 
                    const name = e.target.value;
                    const isValidName = /^[A-Za-z\s]{2,}$/.test(name);
                    setUser({ ...user, 'name': name });
                    
                    if (!isValidName) {
                        e.target.classList.add('error');
                    } else {
                        e.target.classList.remove('error');
                    }
                    }} 
                    defaultValue={user?.name}
                >
                </textarea>
            </h2>

            <h2 className='user-info-header'>
                Email <textarea 
                    onChange={(e) => { 
                    if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e.target.value)) {
                        setUser({ ...user, 'email': e.target.value }) 
                        e.target.classList.remove('error');
                    } else {
                        e.target.classList.add('error');
                    }
                    }} 
                    defaultValue={user?.email}
                >
                </textarea>
            </h2>
        </div>
    )
}

export default UserPage;
