import React from 'react'

const ListItem = ({user}) => {
    return (
        <div>
            <h3>
                {user.name}
            </h3>
        </div>
    )
}

export default ListItem