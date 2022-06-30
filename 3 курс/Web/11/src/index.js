import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import Topic from "./Topic";
import Header from "./Header";
import Text from "./Text";
import Image from "./Image";
import Like from "./Like";

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(
  <StrictMode>
    <Topic />
    <Image />
    <Header />
    <Text />
    <Like />
  </StrictMode>
);
