import React from 'react';
import { useLocation } from 'react-router-dom';

const Header = () => {
const location = useLocation();
const isItemsPage = location.pathname.includes('/items');
const isItemsPageCreateHeader = location.pathname.includes('/item');

return (
    <div className='app-header'>
        <h1>{isItemsPage || isItemsPageCreateHeader ? 'Auction' : 'User list'}</h1>
    </div>
);
};

export default Header;
