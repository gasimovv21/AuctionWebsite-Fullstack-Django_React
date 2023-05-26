import { Route, HashRouter as Router } from "react-router-dom";
import './App.css';
import Header from './components/Header';
import ItemPage from './pages/ItemPage';
import ItemsListPage from './pages/ItemsListPage';
import UserPage from './pages/UserPage';
import UsersListPage from './pages/UsersListPage';

function App() {
  return (
    <Router>
      <div className="container dark">
        <div className="app">
          <Header />
          <Route path="/users" exact component={UsersListPage} />
          <Route path="/user/:id" component={UserPage} />
          <Route path="/items" component={ItemsListPage} />
          <Route path="/item/:id" component={ItemPage} />
        </div>
      </div>
    </Router>
  );
}

export default App;
