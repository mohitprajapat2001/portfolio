/**
 * Navbar component for the application.
 * @returns {JSX.Element} The rendered navbar.
 */
import React from "react";
import { cn } from "@/lib/utils";
import type { IconProps } from "@/utils/types";

/**
 * Icons for the navbar.
 */
import {
    FileUserIcon,
    ArrowRightIcon,
    HomeIcon,
    InfoIcon,
    FolderKanbanIcon,
    PackageOpenIcon,
    RssIcon,
    MailIcon,
    GithubIcon,
    YoutubeIcon,
    LinkedinIcon,
    SmartphoneIcon,
} from "lucide-react";
/**
 * Components for the navbar.
 */
import { Link } from "react-router-dom";
import { buttonVariants } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import {
    Tooltip,
    TooltipContent,
    TooltipProvider,
    TooltipTrigger,
} from "@/components/ui/tooltip";
import { RainbowButton } from "@/components/magicui/rainbow-button";
import { Dock, DockIcon } from "@/components/magicui/dock";
import { ModeToggle } from "@/components/theme/mode-toggle";

const Icons = {
    home: (props: IconProps) => <HomeIcon {...props} />,
    info: (props: IconProps) => <InfoIcon {...props} />,
    project: (props: IconProps) => <FolderKanbanIcon {...props} />,
    contributions: (props: IconProps) => <PackageOpenIcon {...props} />,
    blog: (props: IconProps) => <RssIcon {...props} />,
    github: (props: IconProps) => <GithubIcon {...props} />,
    email: (props: IconProps) => <MailIcon {...props} />,
    linkedin: (props: IconProps) => <LinkedinIcon {...props} />,
    youtube: (props: IconProps) => <YoutubeIcon {...props} />,
    smartphone: (props: IconProps) => <SmartphoneIcon {...props} />,
};

const DATA = {
    navbar: [
        { href: "/#", icon: HomeIcon, label: "Home" },
        { href: "#aboutme", icon: InfoIcon, label: "About" },
        { href: "#projects", icon: FolderKanbanIcon, label: "Projects" },
        { href: "#contributions", icon: PackageOpenIcon, label: "Contributions" },
        { href: "#blogs", icon: RssIcon, label: "Blog" },
    ],
    contact: {
        email: {
            name: "Send Email",
            url: "mailto:mohitdevelopment2001@gmail.com",
            icon: Icons.email,
        },
        phone: {
            name: "Call Me",
            url: "tel:+917877287800",
            icon: Icons.smartphone,
        },
        social: {
            GitHub: {
                name: "GitHub",
                url: "https://github.com/mohitprajapat2001/",
                icon: Icons.github,
            },
            LinkedIn: {
                name: "LinkedIn",
                url: "https://www.linkedin.com/in/itsmohitprajapat/",
                icon: Icons.linkedin,
            },
            Youtube: {
                name: "Youtube",
                url: "https://www.youtube.com/@itsmohitcodes",
                icon: Icons.youtube,
            },
        },
    },
};

/**
 * The main navbar component for the website.
 * It renders a dock of icons which when clicked navigate to the corresponding section.
 * The dock is rendered in the middle of the screen.
 * The icons are rendered as a circle with a size of 12.
 * The icons are also rendered with a tooltip which displays the name of the section.
 * The dock is rendered with a vertical separator in the middle.
 * The dock is rendered with the theme toggle button at the end.
 * @returns {JSX.Element} The rendered navbar.
 */
export default function Navbar(): React.JSX.Element {

    return (
        <nav className="p-4 w-full flex justify-between items-center sticky top-0 z-50">
            <div className="shadow-md rounded-2xl">
                <TooltipProvider>
                    <Dock direction="middle" className="m-0">
                        {DATA.navbar.map((item) => (
                            <DockIcon key={item.label}>
                                <Tooltip>
                                    <TooltipTrigger asChild>
                                        <Link
                                            to={item.href}
                                            aria-label={item.label}
                                            className={cn(
                                                buttonVariants({ variant: "ghost", size: "icon" }),
                                                "size-12 rounded-full",
                                            )}
                                        >
                                            <item.icon className="size-4" />
                                        </Link>
                                    </TooltipTrigger>
                                    <TooltipContent>
                                        <p>{item.label}</p>
                                    </TooltipContent>
                                </Tooltip>
                            </DockIcon>
                        ))}
                        <Separator orientation="vertical" className="h-full" />
                        {Object.entries(DATA.contact.social).map(([name, social]) => (
                            <DockIcon key={name}>
                                <Tooltip>
                                    <TooltipTrigger asChild>
                                        <Link
                                            to={social.url}
                                            aria-label={social.name}
                                            target="_blank"
                                            className={cn(
                                                buttonVariants({ variant: "ghost", size: "icon" }),
                                                "size-12 rounded-full",
                                            )}
                                        >
                                            <social.icon className="size-4" />
                                        </Link>
                                    </TooltipTrigger>
                                    <TooltipContent>
                                        <p>{name}</p>
                                    </TooltipContent>
                                </Tooltip>
                            </DockIcon>
                        ))}
                        <Separator orientation="vertical" className="h-full py-2" />
                        <DockIcon>
                            <Tooltip>
                                <TooltipTrigger asChild>
                                    <ModeToggle />
                                </TooltipTrigger>
                                <TooltipContent>
                                    <p>theme</p>
                                </TooltipContent>
                            </Tooltip>
                        </DockIcon>
                    </Dock>
                </TooltipProvider>
            </div>
            <div className="group transition-all ease-in hover:cursor-pointer">
                <RainbowButton>
                    <FileUserIcon className="size-3" />
                    <span>Download Resume</span>
                    <ArrowRightIcon className="ml-1 size-3 transition-transform duration-300 ease-in-out group-hover:translate-x-0.5" />
                </RainbowButton>
            </div>
        </nav>
    )
};
