import { PayPalButtons, PayPalScriptProvider } from "@paypal/react-paypal-js";
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';


let getTime = (item) => {
    return new Date(item.updated_at).toLocaleDateString()
}

const ListItemAuction = ({ item }) => {
const [clientId, setClientId] = useState('');

useEffect(() => {
    const getPayPalToken = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8002/api/paypal_detail');
        const data = await response.json();
        const token = data.paypal_client_id;
        setClientId(token);
    } catch (error) {
        console.error('Ошибка при получении токена PayPal:', error);
    }
    };

    getPayPalToken();
}, []);

return (
    <Link to={`item/${item.id}`}>
    <div className='users-list-item'>
        <h3>{item.name}</h3>
        <p>
        <span>
            Added to auction: {getTime(item)} Price: {item.price} $ Owner: {item.item_owner}
        </span>
        </p>
        {clientId && (
        <PayPalScriptProvider options={{ 'client-id': clientId }}>
            <div style={{ width: '50px' }}>
            <PayPalButtons
                style={{
                color: 'gold',
                shape: 'rect',
                label: 'paypal',
                layout: 'horizontal',
                }}
                createOrder={(data, actions) => {
                return actions.order.create({
                    purchase_units: [
                    {
                        amount: {
                        value: item.price,
                        },
                    },
                    ],
                });
                }}
                onApprove={(data, actions) => {
                return actions.order.capture().then(function (details) {
                    alert('Transaction completed by ' + details.payer.name.given_name);
                });
                }}
            />
            </div>
        </PayPalScriptProvider>
        )}
    </div>
    </Link>
    );
};

export default ListItemAuction;