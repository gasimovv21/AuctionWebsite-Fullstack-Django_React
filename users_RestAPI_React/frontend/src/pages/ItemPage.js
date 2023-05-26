import Cookies from 'js-cookie';
import React, { useEffect, useState } from 'react';
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg';


const ItemPage = ({ match, history }) => {

    let itemId = match.params.id
    let  [item, setItem] = useState(null)
    let [users, setUsers] = useState([])
    const [selectedOption, setSelectedOption] = useState('');

    const handleOptionChange = (event) => {
        console.log(event.target.value)
        setSelectedOption(event.target.value);
        setItem({ ...item, 'item_owner': event.target.value });
        console.log(item, event.target.value)

    };

    useEffect(() => {
        getItem()
    }, [itemId])

    useEffect(() => {
        getUsers()
    }, [])

    let getUsers = async () => {
        let response = await fetch('api-items/users/')
        let data = await response.json()
        console.log('DATA:', data)
        setUsers(data)
    }

    let getItem = async () => {
        if (itemId === 'new') return


        let reponse = await fetch(`api-items/items/${itemId}`)
        let data = await reponse.json()
        setItem(data)
    }

    let updateItem = async () => {
        const csrftoken = Cookies.get('csrftoken');
    
        fetch(`api-items/items/${itemId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify(item),
        });
    };

    let createItem = async () => {
        const csrftoken = Cookies.get('csrftoken');

        fetch(`api-items/items/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body:JSON.stringify(item)
            
        })
        history.push('/items')
    }

    let deleteItem = async () => {
        const csrftoken = Cookies.get('csrftoken');

        fetch(`api-items/items/${itemId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            }
        })
        history.push('/items')
    }

    let handleSubmit = () => {
        updateItem()
        history.push('/items')
    }


    return (
        <div className='user'>
            <div className='user-header'>
                <h3>
                    <ArrowLeft onClick={handleSubmit} />
                </h3>
                {itemId !== 'new' ? (
                    <button onClick={deleteItem}>Delete</button>
                ) : (
                    <button onClick={createItem}>Done</button>
                )}
            </div>
            <h2 className='user-info-header'>
                Name <textarea 
                    onChange={(e) => { 
                    const name = e.target.value;
                    const isValidName = /^[A-Za-z0-9\s]+$/.test(name);
                    console.log(name)
                    setItem({ ...item, 'name': name });
                    
                    if (!isValidName) {
                        e.target.classList.add('error');
                    } else {
                        e.target.classList.remove('error');
                    }
                    }} 
                    defaultValue={item?.name}
                >
                </textarea>
            </h2>
            <h2 className='user-info-header'>
                Price <textarea 
                    onChange={(e) => { 
                    if (/^\d+(\.\d{2})?$/.test(e.target.value) && parseFloat(e.target.value) >= 1) {
                        console.log(e.target.value)
                        setItem({ ...item, 'price': e.target.value })
                        e.target.classList.remove('error');
                    } else {
                        e.target.classList.add('error');
                    }
                    }} 
                    defaultValue={item?.price}
                >
                </textarea>
            </h2>
            <div>
                <p>Owner: {item?.item_owner}</p>
                <select value={selectedOption} onChange={handleOptionChange}>
                    <option value="">Select owner of item</option>
                    {users.map((user, index) => (
                        <option key={index} value={user.name}>
                            {user.name}
                        </option>
                    ))}
                </select>
                <p>Selected owner: {selectedOption}</p>
            </div>
        </div>
    )
}

export default ItemPage;
