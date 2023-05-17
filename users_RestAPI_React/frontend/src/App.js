import {
  Route,
  HashRouter as Router,
} from "react-router-dom";

import './App.css';
import Header from './components/Header';
import UserPage from './pages/UserPage';
import UsersListPage from './pages/UsersListPage';

function App() {
  return (
    <Router >
      <div className="container dark">
        <div className="app">
          <Header />
          <Route path="/" exact component={UsersListPage} />
          <Route path="/user/:id" component={UserPage} />
        </div>
      </div>
    </Router>
  );
}

export default App;
