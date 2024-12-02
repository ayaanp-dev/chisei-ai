import { Button } from "@/components/ui/button"
import Image from "next/image"
import ShimmerButton from "@/components/ui/shimmer-button";
import { cn } from "@/lib/utils";
import AnimatedGradientText from "../ui/animated-gradient-text";
import SparklesText from "../ui/sparkles-text";
import HeroVideoDialog from "@/components/ui/hero-video-dialog";


export function Hero() {
  return (
    <section className="relative py-20 overflow-hidden bg-primary">
      <div className="container mx-auto px-4 relative z-10">
        <div className="flex flex-col lg:flex-row items-center gap-12">
          <div className="lg:w-1/2 space-y-8">
          <SparklesText text="Revolutionize Your Study Habits with AI" sparklesCount={6} />
          <ul className="text-xl md:text-2xl font-semibold leading-relaxed space-y-2 list-none">
          <li className="flex items-center">
            <span className="mr-2">📚</span> Summarize Complex Notes
          </li>
          <li className="flex items-center">
            <span className="mr-2">✏️</span> Generate Custom Questions
          </li>
          <li className="flex items-center">
            <span className="mr-2">🕒</span> Optimize Study Schedules
          </li>
          <li className="flex items-center">
            <span className="mr-2">📊</span> Track Your Progress
          </li>
          <li className="flex items-center">
            <span className="mr-2">✨</span> AI-Powered Learning
          </li>
        </ul>
            <div className="flex flex-col sm:flex-row gap-4">
            <ShimmerButton className="shadow-2xl" background="#9333ea">
                <span className="whitespace-pre-wrap text-center text-sm font-medium leading-none tracking-tight text-white dark:from-white dark:to-slate-900/10 lg:text-lg">
                    Get Started
                </span>
             </ShimmerButton>
              <Button size="lg" variant="outline" className="text-lg">
                Watch Demo
              </Button>
            </div>
          </div>
          <div className="lg:w-1/2">
            <div className="relative w-full aspect-square">
              <Image
                src="/photos/study.jpg?&width=600"
                alt="Chisei AI Interface"
                layout="fill"
                objectFit="contain"
                className="rounded-lg shadow-2xl"
              />
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
