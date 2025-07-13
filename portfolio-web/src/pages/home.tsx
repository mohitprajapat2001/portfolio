/**
 * Home page component.
 * * @returns {JSX.Element} The rendered home page.
 */
import React from "react";

/**
 * Component representing the home page.
 */
import Navbar from "@/components/custom/navbar";
import AboutMeReveal from "@/components/custom/aboutme";
import AboutMeTerminal from "@/components/custom/terminal-intro";

/**
 * The home page component.
 * It renders a centered, full-width container with no content.
 * @returns {JSX.Element} The rendered home page.
 */
export default function Home(): React.JSX.Element {
    return (
        <div className="flex flex-col items-center justify-center w-6xl mx-auto">
            <Navbar />
            {/* Main content of the home page */}
            <div id="#aboutme" className="grid grid-cols-5 gap-3 justify-center w-full h-full">
                <AboutMeReveal />
                <AboutMeTerminal />
            </div>
            {/* Add more content or components as needed */}
        </div>
    );
}