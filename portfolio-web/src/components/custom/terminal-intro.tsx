import {
    AnimatedSpan,
    Terminal,
    TypingAnimation,
} from "@/components/magicui/terminal";

/**
 * Renders a terminal-like component displaying animated typing text
 * to introduce and describe Mohit Prajapat.
 *
 * The component showcases various typing animations that simulate
 * terminal commands followed by animated text responses. These include:
 * - "whoami" command displaying the name and a waving hand emoji.
 * - "skills --list" command listing programming skills and tools.
 * - "location" command revealing the current geographical location.
 * - "motto" command showing a personal motto.
 * - "exit" command concluding with a closing statement.
 *
 * The animations are styled with delays to create a realistic typing effect.
 * Different spans of text are colored using Tailwind CSS classes.
 */

export default function AboutMeTerminal() {
    return (
        <div className="col-span-2">
            <Terminal>
                {/* Typing animation whoami */}
                <TypingAnimation>&gt; whoami</TypingAnimation>
                <AnimatedSpan delay={1500} className="text-green-500">
                    <span>
                        Mohit Prajapat <span className="text-slate-500">👋</span>
                    </span>
                </AnimatedSpan>
                {/* Typing animation skills */}
                <TypingAnimation delay={2000}>&gt; skills --list</TypingAnimation>
                <AnimatedSpan delay={2500} className="text-green-500">
                    <span>🧠 Python, Django, DRF, PostgreSQL, ElasticSearch.</span>
                </AnimatedSpan>
                <AnimatedSpan delay={3000} className="text-green-500">
                    <span>🚀 Docker, AWS, GitHub Actions.</span>
                </AnimatedSpan>
                <AnimatedSpan delay={3500} className="text-green-500">
                    <span>🎨 React, TailwindCSS, shadcn/ui.</span>
                </AnimatedSpan>
                <AnimatedSpan delay={4000} className="text-green-500">
                    <span>🧪 Pytest, Postman.</span>
                </AnimatedSpan>
                <AnimatedSpan delay={4500} className="text-green-500">
                    <span>📦 Published: django-otp-keygen, django-admin-bulk-io</span>
                </AnimatedSpan>
                {/* Typing animation location */}
                <TypingAnimation delay={5000}>&gt; location</TypingAnimation>
                <AnimatedSpan delay={5500} className="text-green-500">
                    <span>📍 Ahmedabad, Gujrat, India</span>
                </AnimatedSpan>
                {/* Typing animation motto */}
                <TypingAnimation delay={6000}>&gt; motto</TypingAnimation>
                <AnimatedSpan delay={6500} className="text-green-500">
                    <span className="italic">🎯 Keep it clean. Keep it scalable.</span>
                </AnimatedSpan>
                {/* Typing animation exit */}
                <TypingAnimation delay={7000}>&gt; exit</TypingAnimation>
                <AnimatedSpan delay={7500} className="text-green-500">
                    <span>Good code speaks louder than resumes.</span>
                </AnimatedSpan>
            </Terminal>
        </div>
    );
}
