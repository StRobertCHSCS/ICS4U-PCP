using UnityEngine;
using System.Collections;

[RequireComponent (typeof (Rigidbody))]
[RequireComponent (typeof (CapsuleCollider))]

public class RigidbodyFPSWalker : MonoBehaviour{

	public float speed = 10.0f;
	public float gravity = 10.0f;
	public float maxVelocityChange = 10.0f;
	public bool canJump = true;
	public float jumpHeight = 2.0f;
	public float thrust = 4;
	public float limit = 1.0f;
	public float chaseLimit;
	public Rigidbody jetpackUser;
	public bool isJumping = false;
	public float regenFactor = 4f;
	public float deprecFactor = 2f;
	private bool grounded = false;
	private bool isFlying = false;
	private bool inAir = false;
	private bool gotFuel = true;
	private float chaseThrust;

	public float air_accelerate = 5f;
	public float ground_accelerate = 10f;
	public float max_velocity_air = 20f;
	public float max_velocity_ground = 5f;
	public float friction = 0.5f;


	void Awake () {
		GetComponent<Rigidbody>().freezeRotation = true;
		GetComponent<Rigidbody>().useGravity = false;
	}

	void Start(){
		chaseLimit = limit;
		chaseThrust = thrust;
	}

	void FixedUpdate () {
		EnemyAI.targetPosition = transform.position;
		if (isJumping || inAir) {
			inAir = true;
			grounded = false;
		} else {
			inAir = false;
			grounded = true;
		}
		JetpackFuel ();
		Jetpack ();


		if (grounded || inAir || isJumping) {
			// Calculate how fast we should be moving
			Vector3 targetVelocity = new Vector3(Input.GetAxis("Horizontal"), 0, Input.GetAxis("Vertical"));
			targetVelocity = transform.TransformDirection(targetVelocity);
			targetVelocity *= speed;

			// Apply a force that attempts to reach our target velocity
			Vector3 velocity = GetComponent<Rigidbody>().velocity;
			Vector3 velocityChange = (targetVelocity - velocity);
			velocityChange.x = Mathf.Clamp(velocityChange.x, -maxVelocityChange, maxVelocityChange);
			velocityChange.z = Mathf.Clamp(velocityChange.z, -maxVelocityChange, maxVelocityChange);
			velocityChange.y = 0;
			GetComponent<Rigidbody>().AddForce(velocityChange, ForceMode.VelocityChange);


			if (canJump && Input.GetButtonDown ("Jump") && grounded) {
				GetComponent<Rigidbody> ().velocity = new Vector3 (velocity.x, CalculateJumpVerticalSpeed (), velocity.z);
				isJumping = true;
			} 
			else if (inAir && Input.GetButton("Jump")) {
				isJumping = true;
			}
			else {
				isJumping = false;
			}

		}


		// We apply gravity manually for more tuning control
		GetComponent<Rigidbody>().AddForce(new Vector3 (0, -gravity * GetComponent<Rigidbody>().mass, 0));
		grounded = false;
	}


	void OnCollisionStay (Collision col) {
		if (col.gameObject.tag == "Terrain" || col.gameObject.tag == "Wood") {
			grounded = true;
			inAir = false;
		} 
	}

	void JetpackFuel() {
		bool fullTank = false;

		if (chaseLimit < 0) {
			gotFuel = false;
			fullTank = false;
			chaseLimit = 0;
		} else if (chaseLimit == limit) {
			fullTank = true;
			gotFuel = true;
		} else {
			gotFuel = true;
			fullTank = false;
		}

		if (isFlying) {
			chaseLimit -= Time.deltaTime / (deprecFactor / 2f);
		} else if (!fullTank && (grounded || Input.GetButtonDown("Jump"))) {

			if (limit - chaseLimit <= 0.01f) {
				chaseLimit = limit;
			} else {
				chaseLimit += Time.deltaTime / regenFactor;
			}

		} 

	}

	void Jetpack() {
		Vector3 velocity = GetComponent<Rigidbody>().velocity;
		float jumpSpeed = 1f;
		if (Input.GetButton ("Fire2") && gotFuel && chaseLimit > 0) {
			jumpSpeed = thrust * chaseLimit;
			jetpackUser.velocity = new Vector3 (velocity.x, jumpSpeed, velocity.z);
			inAir = true;
			isFlying = true;
		} else {

			isFlying = false;
		}

	}

	float CalculateJumpVerticalSpeed () {
		// From the jump height and gravity we deduce the upwards speed 
		// for the character to reach at the apex.
		return Mathf.Sqrt(2 * jumpHeight * gravity);
	}
}