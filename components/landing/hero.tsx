import { Button } from "@/components/ui/button"
import Image from "next/image"
import ShimmerButton from "@/components/ui/shimmer-button";
import { cn } from "@/lib/utils";
import AnimatedGradientText from "../ui/animated-gradient-text";

export function Hero() {
  return (
    <section className="relative py-20 overflow-hidden">
      <div className="absolute inset-0 z-0">
        <Image
          src="/placeholder.svg?height=600&width=1200"
          alt="AI Study Background"
          layout="fill"
          objectFit="cover"
          quality={100}
          className="opacity-10"
        />
      </div>
      <div className="container mx-auto px-4 relative z-10">
        <div className="flex flex-col lg:flex-row items-center gap-12">
          <div className="lg:w-1/2 space-y-8">
          <AnimatedGradientText>
            <h1 className="md:text-7xl font-bold">
            <span
          className={cn(
            `inline animate-gradient bg-gradient-to-r from-[#ffaa40] via-[#9c40ff] to-[#ffaa40] bg-[length:var(--bg-size)_100%] bg-clip-text text-transparent`,
          )}
        >Revolutionize Your Study Habits with AI</span>
            </h1>
            </AnimatedGradientText>
            <p className="text-xl md:text-2xl text-muted-foreground">
              Chisei AI empowers students to learn smarter, not harder. Summarize notes, generate practice questions, and optimize your study schedule with the power of artificial intelligence.
            </p>
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
                src="/placeholder.svg?height=600&width=600"
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
