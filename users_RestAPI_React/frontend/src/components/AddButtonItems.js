import React from 'react'
import { Link } from 'react-router-dom'
import { ReactComponent as AddIcon } from '../assets/add.svg'

const AddButtonItems = () => {
    return (
        <Link to='/item/new' className='floating-button'>
            <AddIcon />
        </Link>
    )
}

export default AddButtonItems