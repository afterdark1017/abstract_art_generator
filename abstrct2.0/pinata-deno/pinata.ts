import { PinataSDK } from "npm:pinata";
import "jsr:@std/dotenv/load";

export const pinata = new PinataSDK({
	pinataJwt: Deno.env.get("PINATA_JWT"),
	pinataGateway: Deno.env.get("GATEWAY_URL"),
});