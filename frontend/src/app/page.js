import Image from "next/image";
import Temp from "./Components/Temp";

export default function Home() {
  return (
   <>
   <div className="py-3 w-[90%] mx-auto">
    <Temp/>
   </div>
   </>
  );
}
