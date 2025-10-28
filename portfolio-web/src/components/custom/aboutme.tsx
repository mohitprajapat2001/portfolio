/**
 * AboutMeReveal Component
 * This component renders an "About Me" section with a heading, subheading, and avatars.
 */
import { BoxReveal } from "@/components/magicui/box-reveal";
import { InteractiveHoverButton } from "@/components/magicui/interactive-hover-button";
import { Link } from "react-router-dom";


/**
 * A component that renders a simple "About Me" section on the homepage.
 *
 * This component renders a heading, a subheading, and a button. The
 * heading and subheading are revealed using the BoxReveal component, and
 * the button is also revealed using the same component.
 *
 * The boxColor and duration props of the BoxReveal component are
 * overridden to ensure that the box color is #5046e6 and the animation
 * duration is 0.5 seconds.
 *
 * @returns A JSX.Element representing the About Me section.
 */

export default function AboutMeReveal() {
    return (
        <div className="size-full col-span-3 items-center justify-center overflow-hidden pt-8">
            <BoxReveal boxColor={"#5046e6"} duration={0.5}>
                <p className="text-[3.5rem] font-semibold">
                    Minimal code. <br />
                    <span className="text-[#5046e6]">Maximum impact.</span>
                </p>
            </BoxReveal>

            <BoxReveal boxColor={"#5046e6"} duration={0.5}>
                I'm Mohit Prajapat, a backend-focused developer based in Abu Road, Rajasthan. I work with Django, DRF, and PostgreSQL to build fast, scalable systems.
            </BoxReveal>

            <BoxReveal boxColor={"#5046e6"} duration={0.5}>
                <div className="mt-6">
                    <p>
                        I'm passionate about clean architecture, automation, and writing code that just works.
                    </p>
                </div>
            </BoxReveal>
            <Link target="_blank" to="https://github.com/mohitprajapat2001/">
                <InteractiveHoverButton className="mt-5">
                    Check out Github Profile
                </InteractiveHoverButton>
            </Link>
        </div>
    );
}
