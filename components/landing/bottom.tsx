import Image from 'next/image';
import { FlipWords } from '@/components/ui/flip-words';
import { MoveRight, PhoneCall } from "lucide-react";
import { Button } from "@/components/ui/button";

export function Bottom() {
  
    const words = ["torturous", "agonizing", "miserable", "traumatic"];

  return (
    <div className="relative z-20 pb-7 lg:pb-28 max-w-7xl mx-auto">
      <div className="text-4xl mx-auto font-normal text-neutral-600 dark:text-neutral-400 text-center">
        Join us in making studying <span>less</span>
        <FlipWords words={words} />
      </div>
      <div className="flex flex-row gap-3 justify-center mt-8">
        <Button size="lg" className="gap-4" variant="outline">
          Jump on a call <PhoneCall className="w-4 h-4" />
        </Button>
        <Button size="lg" className="gap-4">
          Sign up here <MoveRight className="w-4 h-4" />
        </Button>
      </div>
    </div>
  );
}