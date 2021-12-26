import '../index.css';
import '../App.css';
import 'react-pro-sidebar/dist/css/styles.css';
import {SidemenuData} from './SidemenuData';
import {Link} from 'react-router-dom';

function SideMenu() {
    return (
    <div className="Sidemenu">
      <ul className="SidemenuList">
      {SidemenuData.map((val, key) => {
              return (
                <li key={key} className="row">
                  <Link to={val.link}>
                    <div id="icon">{val.icon}</div> {" "}
                    <span><div id="title">{val.title}</div> </span>
                  </Link>
                </li>
              );
            })}
    </ul>
    </div>
    );
  
}

export default SideMenu;