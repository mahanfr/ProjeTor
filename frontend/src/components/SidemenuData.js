import React from 'react'
import { AiFillHome } from "react-icons/ai";
import { AiFillDashboard } from "react-icons/ai";
import { AiFillProject } from "react-icons/ai";
import { FaUserFriends } from "react-icons/fa";
import { RiTimerFill } from "react-icons/ri";

export const SidemenuData = [
{
title: "Home",
icon:<AiFillHome/>,
link: "/"
},
{
title: "Dashboard",
icon:<AiFillDashboard/>,
link: "/dashboard"
},
{
title: "Projects",
icon:<AiFillProject/>,
link: "/projects"
},
{
title: "Team",
icon:<FaUserFriends/>,
link: "/team"
},
{
title: "Time",
icon:<RiTimerFill/>,
link: "/time"
},
         
    ];

