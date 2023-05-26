import React, { useEffect, useState } from 'react';
import AddButtonItems from '../components/AddButtonItems';
import ListItemAuction from '../components/ListItemAuction';

const ItemsListPage = () => {

    let [items, setItems] = useState([])

    useEffect(() => {
        getItems()
    }, [])


    let getItems = async () => {
        let response = await fetch('/api-items/items/')
        let data = await response.json()
        console.log('DATA:', data)
        setItems(data)
    }

    return (
        <div className='users'>
            <div className='users-header'>
                <h2 className='users-title'>&#9782; Auicton Items</h2>
                <a className='btn-redirect' href='http://localhost:3000/#/users'>Users</a>
                <p className='users-count'>{items.length}</p>
            </div>

            <div className='users-list'>
                {items.map((item, index) => (
                        <ListItemAuction key={index} item={item} />
                ))}
            </div>
            <AddButtonItems />
        </div>
    )
}

export default ItemsListPage